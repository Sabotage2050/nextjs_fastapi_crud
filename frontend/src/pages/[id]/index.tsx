import { useEffect, useState } from "react";
import { useRouter } from "next/router";
import axios from "axios";
import Link from "next/link";
import Todo from "@/components/Todo";
import { TodoType } from "@/types/Todo";
import EditTodoForm from "@/components/EditTodoForm";
import DeleteTodoButton from "@/components/DeleteTodoButton";
import { apiClient } from "@/utils/apiClient";

// Todo詳細ページを表示するコンポーネント
const TodoDetail = () => {
  // ルーティング情報を取得する
  const router = useRouter();
  const { id } = router.query;

  // Todo情報を管理するState
  const [todo, setTodo] = useState<TodoType | null>(null);

  // idが変更されたら(=Todo詳細ページを開いたら)、Todoを取得する
  useEffect(() => {
    // Todoを取得する関数
    const fetchTodo = async () => {
      try {
        // APIからTodoを取得してStateにセットする
        const res = await apiClient.get(`item/${id}`);
        setTodo(res.data);
      } catch (err) {
        console.log(err);
      }
    };

    // idが存在する場合のみ、Todoを取得する
    if (id) {
      fetchTodo();
    }
  }, [id]);

  // Todoを取得中の場合は「Loading...」を表示する
  if (!todo) {
    return <div>Loading...</div>;
  }

  return (
    <div className="m-5">
      <EditTodoForm id={todo.item_id} todo={todo} />
      <DeleteTodoButton id={todo.item_id} />
      <div className="mt-5 bg-green-700 text-white rounded-md w-10">
        <Link href="/" className="">
          Back
        </Link>
      </div>
    </div>
  );
};

export default TodoDetail;
