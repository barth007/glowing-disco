class Stack {
    constructor() {
      this.items = [];
    }
  
    push(element) {
      this.items.push(element);
    }
  
    pop() {
      if (this.items.length === 0) {
        return "Underflow";
      }
      return this.items.pop();
    }
  
    peek() {
      return this.items[this.items.length - 1];
    }
  
    isEmpty() {
      return this.items.length === 0;
    }
  }


  function evaluatePostfixExpression(postfixExpression) {
    const stack = new Stack();
    const tokens = postfixExpression.split(' ');
  
    for (let token of tokens) {
      if (!isNaN(parseFloat(token))) {
        stack.push(parseFloat(token));
      } else {
        const operand2 = stack.pop();
        const operand1 = stack.pop();
        switch (token) {
          case '+':
            stack.push(operand1 + operand2);
            break;
          case '-':
            stack.push(operand1 - operand2);
            break;
          case '*':
            stack.push(operand1 * operand2);
            break;
          case '/':
            stack.push(operand1 / operand2);
            break;
          default:
            break;
        }
      }
    }
  
    return stack.peek();
  }
  

  // Define a postfix expression
const postfixExpression = '3 4 + 5 *';

// Call the evaluatePostfixExpression function with the expression
const result = evaluatePostfixExpression(postfixExpression);

// Output the result
console.log('Result:', result);