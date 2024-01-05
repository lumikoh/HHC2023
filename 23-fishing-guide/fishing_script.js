// ==UserScript==
// @name         Automatic Fishing for HHC2023
// @namespace    http://tampermonkey.net/
// @version      2023-12-18
// @description  Catches fishes automatically in HHC2023. This script is to be used with TamperMonkey.
// @require      http://code.jquery.com/jquery-1.11.3.min.js
// @author       Lumiko
// @match        https://2023.holidayhackchallenge.com/
// @icon         https://free-images.com/or/4384/fish_icon_svg.jpg
// @grant        none
// ==/UserScript==

setInterval(function() {
  let iframes = document.getElementsByClassName('sea-frame');
  if(iframes.length > 0) {
    let iframe = iframes[0].contentDocument;
    let elements = iframe.getElementsByClassName("reelitin");

    if(elements.length > 0) {
        let reelButton = elements[0];
        if(reelButton.style.display === 'none') {
            let castElements = iframe.getElementsByClassName('castreel');
            if(castElements.length > 0) {
                if(castElements[0].style.display !== 'none') {
                    castElements[0].click();
                }
            }
        }
        else {
            let fishOnHook = iframe.getElementsByClassName('gotone');
            if(fishOnHook.length > 0) {
                fishOnHook[0].click();
            }
        }
    }
  }

}, 200);