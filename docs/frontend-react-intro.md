# Intro to React (Beginner Companion Guide)

This document is a beginner-friendly introduction to building web apps with **React**, designed for people who already understand basic HTML/CSS/JavaScript concepts.

## What is React?

React is a JavaScript library for building user interfaces.

Instead of manually updating the page with JavaScript, React lets you:

> **Describe what the UI should look like based on data, and React keeps it updated automatically.**


### The key idea

In traditional JavaScript:
> You manually update the DOM when something changes.

In React:
> You update data, and React updates the UI for you.


### Example idea

Instead of:
- Find element
- Change text
- Update UI manually

You do:
- Change state
- React re-renders UI automatically


## Components: building blocks of React

React apps are made of **components**.

A component is just a JavaScript function that returns UI.

Example:

    tsx
    function Hello() {
      return <h1>Hello World</h1>
    }

Think of components like:

-   Reusable UI blocks
-   Like LEGO pieces for your interface

### Why components matter

## Why components matter

Instead of one giant HTML page, you break your UI into:

-   Navbar
-   Sidebar
-   Cards
-   Buttons
-   Lists

Each piece is independent and reusable.

## JSX: HTML inside JavaScript

React uses JSX, which looks like HTML but lives in JavaScript.

Example:

    return  <h1>Hello</h1>

JSX lets you:

-   Write UI in a familiar HTML-like way
-   Embed JavaScript inside it

Example:

    return  <h1>Hello {name}</h1>

## State: data that changes over time

State is one of the most important React concepts.

> State is data that affects what the UI looks like and can change over time.

Example:

    const [count, setCount] =  useState(0)

-   `count` = current value
-   `setCount` = function to update it

### How state works

When state changes:

1.  React re-runs the component
2.  UI updates automatically
3.  You do NOT manually update the DOM

Example:

    <button  onClick={() => setCount(count  +  1)}>  
	    Count: {count}  
    </button>

## Props: passing data between components

Props are how components receive data.

> Props are inputs to a component.

Example:

    function  Greeting(props) {  
      return  <h1>Hello {props.name}</h1>  
    }

Used like:

    <Greeting  name="Michael"  />


### Key idea

-   Props flow **down**
-   Data is passed from parent → child
-   Props are read-only inside the child

## State vs Props

Concept:

 - State - Data a component owns 
 - Props - Data passed into a component

Simple analogy:

-   State = internal memory
-   Props = information passed in

## useEffect: handling side effects

Some things happen outside rendering, such as:

-   fetching data
-   timers
-   browser APIs

These are handled with `useEffect`.

----------

Example: fetch data on load

    useEffect(() => {  
      fetch("/api/data")  
      .then(res => res.json())  
      .then(data => setData(data))  
    }, [])

### When useEffect runs

 - Runs after the component renders 
 - Runs again if dependencies change


### Key idea

> useEffect is for syncing React with the outside world.

## Rendering model (important mental model)

React works like this:

1.  State changes
2.  Component re-renders
3.  UI updates automatically

> You describe the UI, React handles updates.


