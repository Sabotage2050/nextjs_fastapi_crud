export type  TestItem = Pick<TestItemResponse, "text">

export interface TestItemResponse {
    text: string,
}