# Meal Prep Digital Assistant

Reduce the stress of making family dinners, eat better food, and cut your grocery bill with a meal prep routine aided by a digital assistant.

## Overview
If you are a working parent cooking for your family, you know the stress of figuring out what is for dinner. What should I make tonight? Do I have the ingredients? Do I have to run to the closest grocery store to get what I am missing? Will it taste ok? Will the kids eat it?

A better way to make family dinners is to bulk prep meals on the weekend and heat the meals right before dinner every plan. So, you plan, shop, and cook once.


## Digital Assistant App

This digital assistant is your weekly meal prep co-pilot. It has a bank of recipes for you to choose from. It can help select meals for each day. It can compile a grocery list for you. It can give cooking instructions while you prep and heating instructions on weekdays.

<img width="1447" alt="image" src="https://github.com/user-attachments/assets/1c89ab0e-7c9b-4743-ac49-4ca0b37c1e36" />

<img width="827" alt="image" src="https://github.com/user-attachments/assets/f39b36a8-d7da-4b45-8a09-00d8429c4414" />

<img width="839" alt="image" src="https://github.com/user-attachments/assets/a9be340e-c29a-4b99-802b-7202697b74b2" />

<img width="881" alt="image" src="https://github.com/user-attachments/assets/cd31c4f7-afb4-4a8d-b9a3-c6565b25a722" />



## How It Works
The assistant has two components: a recipe aggregation tool and a Claude project with relevant meal prep context. The aggregation tool compiles recipes from several PDF documents provided by you into one. The Anthropic-hosted project uses the compiled document and a description of meal prep activities, also known as "system prompt", to answer questions.

## Considerations
The assistant doesn't have memory across chats yet. So, for example, if you want the assistant to remember the list of meals you want to make this week, you have to add the list to the Claude project manually.
