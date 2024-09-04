require("dotenv").config();
const fs = require("fs");
// import { writeFile } from 'fs'; if you are using a typescript file

const environmentFile = `export const environment = {
  production: false,
  apiServerUrl: "${process.env.API_SERVER_URL}", // the running FLASK api server url
  auth0: {
    url: "${process.env.AUTHO_URL}", // the auth0 domain prefix
    audience: "${process.env.AUTH0_AUDIENCE}", // the audience set for the auth0 app
    clientId: "${process.env.AUTH0_CLIENT_ID}", // the client id generated for the auth0 app
    callbackURL: "${process.env.AUTH0_CALLBACK_URL}", // the base url of the running ionic application.
  },
};
`;

// Generate environment.ts file
fs.writeFile(
  "./src/environments/environment.ts",
  environmentFile,
  function (err) {
    if (err) {
      throw console.error("generated: " + err);
    } else {
      console.log(`Angular environment.ts file generated`);
    }
  }
);
