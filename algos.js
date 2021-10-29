/*
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

// const str1 = "a x a";
// const expected1 = true;

// const str2 = "racecar";
// const expected2 = true;

// const str3 = "Dud";
// const expected3 = false;

// const str4 = "oho!";
// const expected4 = false;



// /**
//  * Determines if the given str is a palindrome (same forwards and backwards).
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @returns {boolean} Whether the given str is a palindrome or not.
//  */
function isPalindrome(str) {
    var newStr = "";
    for(var i = str.length-1; i >= 0; i--){
        newStr += str[i];
    }
    if(newStr === str){
        return true;
    }
    else{
        return false;
    }
}
// console.log(isPalindrome(str3))

const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

const str4 = "a1001x20002y5677765z";
const expected4 = "5677765";

const str5 = "a1001x20002y567765z";
const expected5 = "567765";

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */
function longestPalindromicSubstring(str) {
    var pal = str[0];

    for(var i = 0; i < str.length; i++){
        for(var x = i+1; x < str.length; x++){
            var slice= str.slice(i,x)
            console.log(slice)
            if(isPalindrome(slice)== true && slice.length>pal.length){
                pal=slice
            }
        }
    }
    return pal
}
console.log(longestPalindromicSubstring(str5));
