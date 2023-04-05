import { Publisher } from "./publisher";

export interface PublisherNrBooksDTO{
    id: Publisher | number;
    name: string;
    nrBooksPublished: number;
}