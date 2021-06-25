const path = require('path');
const  webpack  = require('webpack');
var nodeExternals = require('webpack-node-externals');
module.exports = {
    devtool: 'source-map',
    module : {
        rules : [
            {
                test : /\.ts$/,
                exclude : /node_modules/,
                use : {
                    loader: 'ts-loader'
                },
                include : path.resolve(__dirname, 'src')
            }
        ]
    },
    resolve : {
        modules : ['node_modules'],
        extensions : ['.tsx','.ts', '.js']
    },
    output : {
        publicPath : '/',
        filename: 'bundle.js',
        path: path.resolve(__dirname),
    },
    devServer : {
        contentBase : './',
        watchOptions : {
            poll: true
        }
    },
    mode : 'development',
    externals : {
        "socket.io-client": "io"
    }
}