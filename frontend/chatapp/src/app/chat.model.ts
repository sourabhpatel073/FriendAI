export interface Message {
    message: string;
    sender: string;
  }
  
 
  export interface Chat {
    id: number;
    user_id: string;
    messages: {
        message: string;
        sender: string;
    }[];
    date_of_post: string;
    data: string;
    pdfsize: number;
    pdfname: string;
}
