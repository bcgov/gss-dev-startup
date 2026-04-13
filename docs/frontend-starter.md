# Frontend starter
This is a flailing attemt to get people started on the frontend. This proceedure should help incrementally introduce some fundementals of building a super basic frontend with react with typescript.
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

## Minimal Setup (Webpack + Typescript + React)
1. Install core dependencies(these are installed for this project):
    ```shell
    # Install Webpack and TypeScript plumbing
    npm install --save-dev webpack webpack-cli webpack-dev-server typescript ts-loader html-webpack-plugin css-loader style-loader
    # Install React and React router
    npm install react react-dom react-router-dom
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
3. Create a file named **webpack.config.js** in your root directory. This tells Webpack how to handle .ts and .css files.  

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
            <head>
                <title>GSS Frontend Starter</title>
            </head>
            <body>
                <div id="root"></div>
            </body>
        </html>
    ```
2. Create the React Entry Point: Create ```src/index.tsx```
    ```
    import React from 'react';
    import ReactDOM from 'react-dom/client';
    import App from './App';

    const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
    root.render(<App />);
    ```