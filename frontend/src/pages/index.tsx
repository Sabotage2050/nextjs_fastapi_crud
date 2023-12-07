import CreateTodoForm from "@/components/CreateTodoForm";
import Todos from "@/components/Todos";
export default function Home() {
  return (
    <div>
      <CreateTodoForm />
      <Todos />
    </div>
  );
}
