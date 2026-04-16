# \# Intro to Web App Coding - Fundamentals

# 

# Web development is still programming but instead of writing scripts that run top-to-bottom like Python, you’re building systems that \*\*respond to user actions\*\* inside a browser.

# 

# A good mental shift is this:

# 

# > Python: programs usually “\*\*run and finish\*\*”

# Web apps: “\*\*run continuously and react to events\*\*”

# 

# \## The Three Core Technologies

# \### HTML: Structure

# 

# HTML defines the \_content and structure\_ of a webpage.

# 

# \*Example:\*

# 

# &#x20;   <h1>GIS Library</h1>

# &#x20;   <button>Sort</button>

# 

# \*Think:\*

# > “What exists on the page?”

# 

# \### CSS: Styling

# CSS controls how things look.

# 

# \*Example:\*

# 

# &#x20;   button {  

# &#x09;    background-color: blue;  

# &#x09;    color: white;  

# &#x20;   }

# 

# \*Think:\*

# > “How does it look?”

# 

# \### JavaScript: Behavior

# JavaScript is where interactivity happens.

# 

# \*Example:\*

# 

# &#x20;   button.addEventListener("click", () => {  

# &#x09;    console.log("clicked")  

# &#x20;   })

# &#x20; 

# \*Think:\*

# > “What happens when users interact?”

# 

# \## The Big Difference from Python

# In Python you write a script, it runs in order and finishes.

# 

# In Web Apps, code runs continuously in response to events:

# 

# &#x20;- clicks

# &#x20;- typing

# &#x20;- data loading

# &#x20;- page changes

# 

# So instead of "run once", you build \*\*event-driven systems\*\*.

# 

# \## The DOM: The “live document”

# 

# The browser turns HTML into a live structure called the \*\*DOM (Document Object Model)\*\*. This is the browser’s \*\*live, in-memory representation of your HTML page\*\*. It is becomes a \*\*tree of objects in memory\*\*, not a static file.

# 

# !\[DOM HTML tree](https://www.w3schools.com/js/img\_htmltree\_800.png)

# 

# In Python, if you print something:

# 

# &#x20;   print("Hello")

# 

# That’s it. Done.

# 

# In the browser:

# \-   The page is always “alive”

# \-   JavaScript can reach in and change it at any time

# 

# \## Event-driven programming (core concept)

# 

# Web apps are driven by events:

# 

# &#x20;- user clicks a button

# &#x20;- data loads from a server

# &#x20;- input changes

# 

# \*Example:\*

# 

# &#x20;   button.onclick =  function () {  

# &#x09;    alert("Hello")  

# &#x20;   }

# 

# \## State: the missing concept from basic JS

# 

# State is \*\*data that changes over time and affects what the user sees\*\*.

# 

# \*Example:\*

# 

# &#x20;- number of items in an online cart

# &#x20;- selected filter

# &#x20;- loaded layer list

# 

# In regular JavaScript you must manually update the UI when it changes.

# 

# Modern frameworks (like React) automate this relationship.

# 

# \## APIs: how apps get data

# 

# Most web apps don’t store everything locally. They fetch data from servers:

# 

# &#x20;   fetch("/api/gis-data")  

# &#x09;    .then(res => res.json())

# 

# Python analogy:

# &#x20;- similar to "requests.get()"

# &#x20;- but asynchronous and UI-driven

# 

# \## Asynchronous behavior

# 

# Javascript is heavily async. It does not wait for slow operations (like network requests). It keeps running. This is called \*\*non-blocking asynchronous execution\*\*.

# 

# \### Python comparison

# In Python:

# 

# &#x20;   data = requests.get(url)  

# &#x20;   print(data)

# 

# This is \*\*blocking\*\*:

# \-   Code stops

# \-   Waits for response

# \-   Then continues

# 

# \### JavaScript behavior

# 

# In JavaScript:

# 

# &#x20;   fetch("/api/gis-data")  

# &#x20;   console.log("Done")

# 

# What actually happens:

# 

# 1\.  `fetch()` starts request

# 2\.  JavaScript immediately moves on

# 3\.  `"Done"` prints BEFORE data returns

# 

# \### Mental Model

# \#### Python:

# 

# > “Go to the store, wait until I come back, then continue”

# 

# \#### JavaScript:

# 

# > “Go to the store, I’ll come back later—keep doing other things”

# 

# \### Why

# Because in a browser:

# 

# \-   The UI must NEVER freeze

# \-   Users must still be able to click, scroll, type

# 

# So JavaScript says:

# 

# > “Never block the page just because you're waiting for something slow”

# 

# \## Putting it all together

# 

# A simple web app works like this:

# 

# 1\.  HTML defines structure

# 2\.  CSS styles it

# 3\.  JavaScript adds behavior

# 4\.  User interacts (events)

# 5\.  Data changes (state)

# 6\.  UI updates

# 

# \## TLDR

# 

# > Web development is building \*\*event-driven, state-based systems in the browser\*\*, where HTML defines structure, CSS defines appearance, and JavaScript defines behavior and data flow.

