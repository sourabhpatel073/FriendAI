import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
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
}
