import { atom } from "jotai";

import api from "../api";

export const postsAtom = atom(async () => {
  const response = await api.get("/posts/");
  return response.data;
});
