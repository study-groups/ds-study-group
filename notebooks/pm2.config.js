const PORT = 8888;

const TETRA_SRC = process.env.TETRA_SRC || "~/src/devops/tetra";


module.exports = {
  apps: [
    {
      name: `hr-${PORT}-jupyter`,
      script: './entrypoint.sh',
      args: '',
      cwd: './',
      autorestart: true,
      watch: false,
      env: {
        PORT: PORT.toString(),
      },
    },
    {
      name: `hr-${PORT}-tunnel`,
      script: `${TETRA_SRC}/bash/hotrod/tunnel.sh`,
      args: `${PORT}`,
      cwd: './',
      autorestart: true,
      watch: false,
      env: {
        PORT: PORT.toString(),
      },
    },



  ],
};

