# Intro to Web App Coding - Fundamentals

Web development is still programming but instead of writing scripts that run top-to-bottom like Python, you’re building systems that **respond to user actions** inside a browser.

A good mental shift is this:

> Python: programs usually “**run and finish**”
Web apps: “**run continuously and react to events**”

## The Three Core Technologies
### HTML: Structure

HTML defines the _content and structure_ of a webpage.

*Example:*

    <h1>GIS Library</h1>
    <button>Sort</button>

*Think:*
> “What exists on the page?”

### CSS: Styling
CSS controls how things look.

*Example:*

    button {  
	    background-color: blue;  
	    color: white;  
    }

*Think:*
> “How does it look?”

### JavaScript: Behavior
JavaScript is where interactivity happens.

*Example:*

    button.addEventListener("click", () => {  
	    console.log("clicked")  
    })
  
*Think:*
> “What happens when users interact?”

## The Big Difference from Python
In Python you write a script, it runs in order and finishes.

In Web Apps, code runs continuously in response to events:

 - clicks
 - typing
 - data loading
 - page changes

So instead of "run once", you build **event-driven systems**.

## The DOM: The “live document”

The browser turns HTML into a live structure called the **DOM (Document Object Model)**. This is the browser’s **live, in-memory representation of your HTML page**. It is becomes a **tree of objects in memory**, not a static file.

![DOM HTML tree](https://www.w3schools.com/js/img_htmltree_800.png)

In Python, if you print something:

    print("Hello")

That’s it. Done.

In the browser:
-   The page is always “alive”
-   JavaScript can reach in and change it at any time

## Event-driven programming (core concept)

Web apps are driven by events:

 - user clicks a button
 - data loads from a server
 - input changes

*Example:*

    button.onclick =  function () {  
	    alert("Hello")  
    }

## State: the missing concept from basic JS

State is **data that changes over time and affects what the user sees**.

*Example:*

 - number of items in an online cart
 - selected filter
 - loaded layer list

In regular JavaScript you must manually update the UI when it changes.

Modern frameworks (like React) automate this relationship.

## APIs: how apps get data

Most web apps don’t store everything locally. They fetch data from servers:

    fetch("/api/gis-data")  
	    .then(res => res.json())

Python analogy:
 - similar to "requests.get()"
 - but asynchronous and UI-driven

## Asynchronous behavior

Javascript is heavily async. It does not wait for slow operations (like network requests). It keeps running. This is called **non-blocking asynchronous execution**.

### Python comparison
In Python:

    data = requests.get(url)  
    print(data)

This is **blocking**:
-   Code stops
-   Waits for response
-   Then continues

### JavaScript behavior

In JavaScript:

    fetch("/api/gis-data")  
    console.log("Done")

What actually happens:

1.  `fetch()` starts request
2.  JavaScript immediately moves on
3.  `"Done"` prints BEFORE data returns

### Mental Model
#### Python:

> “Go to the store, wait until I come back, then continue”

#### JavaScript:

> “Go to the store, I’ll come back later—keep doing other things”

### Why
Because in a browser:

-   The UI must NEVER freeze
-   Users must still be able to click, scroll, type

So JavaScript says:

> “Never block the page just because you're waiting for something slow”

## Putting it all together

A simple web app works like this:

1.  HTML defines structure
2.  CSS styles it
3.  JavaScript adds behavior
4.  User interacts (events)
5.  Data changes (state)
6.  UI updates

## TLDR

> Web development is building **event-driven, state-based systems in the browser**, where HTML defines structure, CSS defines appearance, and JavaScript defines behavior and data flow.
