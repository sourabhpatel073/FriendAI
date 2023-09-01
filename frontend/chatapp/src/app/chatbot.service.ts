import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class ChatbotService {

  constructor(private http: HttpClient) {}

  askQuestion(query: string) {
    const formData = new FormData();
    formData.append('question', query);
    return this.http.post('http://localhost:8000/galaxy/ask_question/', formData);
  }

  // chatbot.service.ts
saveChatToBackend(chatData: any, userId: string) {
  const apiUrl = "http://localhost:8000/galaxy/chat/create/";  // Replace with your API endpoint URL
  const headers = new HttpHeaders({
      'Content-Type': 'application/json'
  });

  const payload = {
    messages: chatData.messages,
    date_of_post:Date(),
    pdfsize:chatData.pdfsize,
    pdfname:chatData.pdfname,
    user_id: userId
  };
   console.log(payload)
  return this.http.post(apiUrl, payload, { headers: headers });
}

}
