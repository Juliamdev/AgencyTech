// api.ts
import axios from "axios";

export const api = axios.create({
  baseURL: "http://26.215.157.128:8000",
});