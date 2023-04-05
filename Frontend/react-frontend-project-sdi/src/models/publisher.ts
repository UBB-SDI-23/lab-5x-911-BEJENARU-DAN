import { Address } from "./address";

export interface Publisher{
    id: number;
    name: string;
    foundingYear: string;
    email: string;
    address: Address;
    webAddress: string;
}