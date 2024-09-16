import React from "react";
import { useAtom } from "jotai";
import { postsAtom } from "./state/postAtom";

interface Tag {
  id: number;
  name: string;
}

interface Post {
  id: number;
  title: string;
  body: string;
  created_at: string;
  modified_at: string;
  tags: Tag[];
}

const PostList: React.FC = () => {
  const [posts] = useAtom(postsAtom);

  return (
    <div>
      <h1>Blog Posts</h1>
      <ul>
        {posts?.map((post: any) => (
          <li key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.body}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PostList;
