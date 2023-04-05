import { Publisher } from "./publisher";

export interface Book{
    id: number;
    name: string;
    nrOfPages: number;
    publisherID?: Publisher | number;
    releaseYear: number;
    genre: string;
}