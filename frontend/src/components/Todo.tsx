import { TodoType } from "@/types/Todo";

const Todo = ({ todo }: { todo: TodoType }) => {
  return (
    <div className="ml-2 mt-5 text-red-900 max-w-xs text-4xl">
      ・{todo.name}
    </div>
  );
};

export default Todo;
