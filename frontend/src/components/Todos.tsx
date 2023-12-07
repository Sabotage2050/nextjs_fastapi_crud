import { useEffect, useState } from "react";
import axios from "axios";
import { TodoType } from "@/types/Todo";
import Todo from "./Todo";
import Link from "next/link";
import { apiClient } from "@/utils/apiClient";

const Todos = () => {
  const [todos, setTodos] = useState<TodoType[]>([]);

  const fetchTodos = async () => {
    try {
      const res = await apiClient.get<TodoType[]>(`items/`);
      setTodos(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  return (
    <div className="">
      {todos.map((todo) => (
        <Link key={todo.item_id} href={`/${todo.item_id}`} className="">
          <Todo todo={todo} />
        </Link>
      ))}
    </div>
  );
};

export default Todos;
