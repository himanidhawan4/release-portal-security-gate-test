
const crypto = require("crypto");

// Test 1: Dynamic code execution — intentionally insecure
function calculateExpression(userInput) {
    return eval(userInput);
}

// Test 2: Weak hashing algorithm — intentionally insecure
function hashPassword(password) {
    return crypto
        .createHash("md5")
        .update(password)
        .digest("hex");
}

// Test 3: Hardcoded credential — intentionally insecure
const API_KEY = "test_api_key_123456789";

// Test 4: Potential command injection — intentionally insecure
const { exec } = require("child_process");

function checkFile(fileName) {
    exec("ls " + fileName, (error, stdout) => {
        if (error) {
            console.error("Command failed:", error.message);
            return;
        }

        console.log(stdout);
    });
}

// Test 5: Unsafe handling of user-provided HTML
function displayMessage(userMessage) {
    document.getElementById("message").innerHTML = userMessage;
}

// Test 6: Basic function with normal logic
function calculateTotal(price, quantity) {
    if (price < 0 || quantity < 0) {
        throw new Error("Price and quantity must be non-negative");
    }

    return price * quantity;
}

// Test execution
console.log("Expression result:", calculateExpression("2 + 3"));
console.log("MD5 hash:", hashPassword("demo-password"));
console.log("API key configured:", Boolean(API_KEY));
console.log("Sample total:", calculateTotal(100, 2));

// Do not call checkFile() with untrusted input.
// displayMessage() requires a browser DOM to run.
