# wasteZero
Uses Image Recognition to Sort Wastes into their Corresponding Categories

## Inspiration
Waste sorting is a process that has been around for centuries. The goal is to divide wastes into different categories in order to reduce waste and improve recycling and composting to have a cleaner and livable environment for present and future generations. However, a lot of people have been struggling to distinguish between different categories of sorting that their city has provided for them in public. This confusion has caused people to put their trash into whatever category which can result in endangering the environment. Personally, I always have difficulty in knowing which trash bin I'm supposed to put my trash in. To solve this dilemma, I have made this project that recognizes your waste and sorts it into its corresponding category. I was inspired by the "Zero Waste by 2020" that UC Berkeley has been working on and I hope this project can help this process.

## What it does
Using this application, you can upload an image of your trash object on your phone or laptop and then the program tells you whether your waste should go into Compost, Recycle, or Landfill category based on the texture of the item.

## How I built it
I used the Microsoft Computer Vision API's deep learning algorithms with the use of rapidAPI to recognize the image of the trash. I trained the API so that it can recognize the texture of the objects so I can use it to sort them into their categories. After the program recognizes an image, I used the image tags to go through a large data base of possible waste items and then sorted them accordingly.

## Challenges I ran into
This was my first time to use an Image Recognition API and to train an API, so I repeatedly ran into different challenges. I had difficulty in getting the API to work and implement it into my program. Training the API was even harder because the image recognition APIs are usually not good at recognizing the texture of an item; therefore I had to use a lot of pictures to come close to a decent amount of accuracy. Another challenge I ran into was implementing my back-end platform into some sort of front-end application. But going through web, I came across kivy which is a Cross-platform Python Framework for NUI Development and I was able to implement my program into it.

## Accomplishments that I'm proud of
I'm proud that I was able to work by myself and to make a working application that has a great potential of saving our planet by having a cleaner and waste-free environment that the future generation can live on. I have always been a strong advocate of environment, so I'm proud that I was able to use my knowledge to help the society I live in and across the world by reducing the waste and cleaning the environment.

## What I learned
I learned a lot during this project. I learned how to use json files. I learned how to use an image recognition API and train it. I learned how to implement my python project into a front-end application.

## What's next for wasteZero
I'm planning to improve wasteZero so that it can recognize a group of items in one image and tell the user which trash goes to which trash bin category. I'm planning to improve the accuracy of the image recognition. I'd also like to get my project into the app store.
