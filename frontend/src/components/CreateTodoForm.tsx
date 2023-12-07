import { useState } from "react";
import axios from "axios";
import { TodoType } from "@/types/Todo";
import { apiClient } from "@/utils/apiClient";

// Todoを作成するフォーム
const CreateTodoForm = () => {
  // フォームの入力値を管理するstate
  const [name, setName] = useState("");
  const [contents, setContents] = useState("");

  // フォームの入力値を更新する関数
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // e.targetの値が空文字列かどうかをチェックする
    const isInputEmpty = (input: string | null) => {
      if (input === null || input === undefined) {
        return true;
      }
      return input.trim() === "";
    };

    const formData = new FormData(e.currentTarget);
    const name = formData.get("name") as string;
    const contents = formData.get("contents") as string;

    if (isInputEmpty(name) || isInputEmpty(contents)) {
      // エラーメッセージを表示する
      alert("Error: Input cannot be empty");
      return;
    }

    try {
      // APIを呼び出して、Todoを作成する
      await apiClient.post(
        "item",
        {
          name: name,
          contents: contents,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      // Todoの作成に成功したら、フォームの入力値をリセットする
      setName("");
      setContents("");

      // Todoの作成に成功したら画面を更新する(Todoを再取得するため)
      window.location.reload();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="">
      <form onSubmit={handleSubmit} className="flex flex-col">
        <label className="m-2 text-2xl">New Todo</label>
        <input
          type="text"
          name="name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="title"
          className="m-2 border border-black max-w-xs"
        />
        <input
          value={contents}
          type="text"
          name="contents"
          onChange={(e) => setContents(e.target.value)}
          placeholder="Contents"
          className="m-2 border border-black h-20 max-w-md"
        />
        <button
          type="submit"
          className="mt-3 p-1 rounded-md w-20 text-white bg-blue-700"
        >
          Create
        </button>
      </form>
    </div>
  );
};

export default CreateTodoForm;
