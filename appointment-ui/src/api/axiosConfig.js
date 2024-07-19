import axios from "axios";


const restapiurl = import.meta.env.VITE_REST_API_ROOT;

export const COMMON_API_HTTP = axios.create({
  baseURL: restapiurl,
});   

console.log(window.location.pathname);
console.log("axios starts");
COMMON_API_HTTP.defaults.headers.post['Content-Type'] = 'application/json';
COMMON_API_HTTP.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
COMMON_API_HTTP.defaults.headers.common['Access-Control-Allow-Methods']= 'GET,HEAD,OPTIONS,POST,PUT';
COMMON_API_HTTP.defaults.headers.common['Access-Control-Allow-Headers']= 'Origin, X-Requested-With, Content-Type,Accept, x-client-key, x-client-token, x-client-secret, Authorization';

console.log(COMMON_API_HTTP)
export default COMMON_API_HTTP;

