// THIS IS JUST AN EXAMPLE. DO NOT USE IT.

import { config } from "dotenv";

const frontEnvVars = config({ path: "./.env" }).parsed || {};

console.log(frontEnvVars.FRONT_DEBUG);