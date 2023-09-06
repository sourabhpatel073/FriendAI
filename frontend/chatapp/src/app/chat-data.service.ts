import { Injectable } from '@angular/core';
import { Chat } from './chat.model';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatDataService {
  private readonly baseUrl = 'https://friendai.onrender.com/galaxy';

  constructor(private http: HttpClient) { }

  // Fetch all chat histories
  getChatHistories(): Observable<Chat[]> {
    return this.http.get<Chat[]>(`${this.baseUrl}/chat/`);
  }
  deleteChat(chatId: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/chat/delete/${chatId}/`);
  }
  // If you ever need to fetch a specific chat detail by ID, you can use the following method:
  getChatById(id: number): Observable<Chat> {
    return this.http.get<Chat>(`${this.baseUrl}/chat/${id}/`);
  }
}
