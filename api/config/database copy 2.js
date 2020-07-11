module.exports = ({ env }) => ({
  defaultConnection: "default",
  connections: {
    default: {
      connector: "mongoose",
      settings: {
        uri:
          "mongodb://mocorona:rMUkBG84MH4SQRs9@cluster0.ojcws.mongodb.net:27017/mocorona?ssl=true&retryWrites=true&w=majority&authSource=admin",
        database: "mocorona",
      },
      options: {
        ssl: true,
      },
    },
  },
});
