const baseEndpoint = ""; //on production set the base API endpoints to match the Heroku app URL.

const endpoints = {
  new: `${baseEndpoint}/`,
  login: `${baseEndpoint}do-login/`,
  logout: `${baseEndpoint}logout/`,
  check_auth: `${baseEndpoint}check-auth/`,
  register: `${baseEndpoint}register/`,
};

export { endpoints };
