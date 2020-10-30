module.exports = ({ env }) => ({
  defaultConnection: "default",
  connections: {
    default: {
      connector: "mongoose",
      settings: {
        uri: env("DATABASE_URI", "127.0.0.1"),
        database: env("DATABASE_NAME", "mocorona"),
      },
      options: {
        ssl: env.bool("DATABASE_SSL", false),
      },
    },
  },
});
