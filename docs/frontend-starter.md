# Frontend starter
This is a flailing attempt to get people started on the frontend. This procedure should help incrementally introduce some fundamentals of building a super basic frontend with react with typescript.  
```
Engaging in activities where you don't excel can actually be beneficial; it builds resilience and lowers the fear of failure.
```

## The Prequel

1. Install nvm, node.js, and npm for WSL
[Microsoft instructions](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl)

2. Verify your install  
    ```shell
    node -v
    npm -v
    ```
3. Create your project directory  
    ```shell
    mkdir demo-react-frontend
    ```
4. Use npm to initialize your project
    ```shell
    npm init -y
    ```
    ✅ Checkpoint: package.json exists, npm commands work
5. This is the structure we should end up with
    ```
    demo-react-frontend/
    ├─ public/
    ├─ src/
    ├─ webpack.config.js
    ├─ tsconfig.json
    └─ package.json
    ```

## Minimal Setup (Webpack + Typescript + React)
1. Install core dependencies(these are installed for this project):
    ```shell
    # Install Webpack and TypeScript plumbing
    npm install --save-dev webpack webpack-cli webpack-dev-server typescript ts-loader html-webpack-plugin css-loader style-loader
    # Install React and React router
    npm install react@18 react-dom@18 react-router-dom
    npm install --save-dev @types/react @types/react-dom
    # install bc-sans
    npm install @bcgov/bc-sans
    ```

## Configuration

1. Create **package.json** in the root project folder(/demo-react-frontend)
    ```json
    {
    "name": "demo-react-frontend",
    "version": "1.0.0",
    "type": "module",
    "scripts": {
        "start": "webpack serve --mode development --config webpack.config.cjs"
    }
    }
    ```
2. Create **tsconfig.json** in the root project folder(/demo-react-frontend)
    ```json
    {
    "compilerOptions": {
        "target": "ESNext",
        "module": "ESNext",
        "moduleResolution": "bundler",
        "jsx": "react-jsx",
        "strict": true,
        "esModuleInterop": true,
        "skipLibCheck": true,
        "forceConsistentCasingInFileNames": true,
        "allowImportingTsExtensions": true,
        "noEmit": true
    },
    "include": ["src"]
    }
    ```
3. Create a file named **webpack.config.cjs** in your root directory. This tells Webpack how to handle .ts and .css files.  

    ```JavaScript
    const path = require('path');
    const HtmlWebpackPlugin = require('html-webpack-plugin');

    module.exports = {
    entry: './src/index.tsx',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
        clean: true
    },
    resolve: { extensions: ['.ts', '.tsx', '.js'] },
    module: {
        rules: [
        { test: /\.tsx?$/, loader: 'ts-loader', exclude: /node_modules/ },
        { test: /\.css$/, use: ['style-loader', 'css-loader'] }
        ]
    },
    plugins: [ new HtmlWebpackPlugin({ template: './public/index.html' }) ],
    devServer: { port: 3000, historyApiFallback: true }
    };
    ```

## Make some 🩻 content
1. Create a ```public/index.html```. This is the only HTML file the browser actually loads; Webpack will inject our script here.:
    ```html 
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>GSS Frontend Starter</title>
            </head>
            <body>
                <div id="root"></div>
            </body>
        </html>
    ```
2. Create the React Entry Point: Create ```src/index.tsx```
    ```typescript
    import React from 'react';
    import ReactDOM from 'react-dom/client';
    import App from './App';

    const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
    root.render(<App />);
    ```

3. Create your first typescript **src/App.tsx**
    ```typescript
    // src/App.tsx
    export default function App() {
    
    return (
        <>
        <div style={{ padding: '40px' }}>
            <h1>Hello World</h1>
        </div>
        </>
    );
    }
    ```

    Test your frontend
    ```shell
    npm start
    ```
    The app will open at http://localhost:3000.

## Components & Branding
Components allows for modular design and code reuse. For example, lets create a header that will allow all headers in your frontend to be the same.


1. **src/components/Header.tsx**
    ```
    export const Header = () => (
    <header style={{ backgroundColor: '#003366', color: 'white', padding: '10px 30px', borderBottom: '2px solid #fcba19', display: 'flex', alignItems: 'center' }}>
        <img src="https://www2.gov.bc.ca/assets/download/b9ea990680374e50882e987fd762e811/images/gov_bc_logo.svg" alt="BC Logo" width="150" />
        <h2 style={{ marginLeft: '20px' }}>Frontend Training</h2>
    </header>
    );
    ```
2. Update your app to include the header   
    **src/App.tsx**
    ```typescript
    // src/App.tsx
    // import header
    import { Header } from './components/Header';
    import './index.css';
    export default function App() {
    
    return (
        <>
        <Header />
        <div style={{ padding: '40px' }}>
            <h1>Hello World</h1>
        </div>
        </>
    );
    }
    ```
3. Add some style **src/index.css**
    ```css
    @import "@bcgov/bc-sans/css/BCSans.css";
    body { font-family: 'BCSans', sans-serif; margin: 0; background-color: #f2f2f2; }
    ```


## State and UseEffect
We will implement the counter state and useEffect from this [backgrounder](https://github.com/bcgov/gss-dev-startup/blob/main/docs/frontend-react-intro.md#state-data-that-changes-over-time) to this app.  
**src/App.tsx**
```typescript
# src/App.tsx
// import the header component
import { Header } from './components/Header';
import './index.css';
// need this for useState and useEffect
import { useState, useEffect } from 'react';
export default function App() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        console.log(`The count is now: ${count}`);
}, [count]);

return (
    <>
    <Header />
    <div style={{ padding: '40px' }}>
        <h1>Hello World</h1>
        <button onClick={() => setCount(count + 1)}>
            Click Count: {count}
        </button>
    </div>
    </>
);
}
```

