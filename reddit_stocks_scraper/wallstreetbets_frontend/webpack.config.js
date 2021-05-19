module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        exclude: /node_modules/,
        test: /\.(svg|png|jpg|gif)$/,
        use: "file-loader",
      },
    ]
  }
};