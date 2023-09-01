import { Injectable } from '@angular/core';
import { Chat } from './chat.model';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ChatDataService {

  // Mock chat data
  private chats = [
    {
        "id": 1,
        "user_id": "12345",
        "messages": [
            {
                "message": "give summary",
                "sender": "user"
            },
            {
                "message": "The given context includes...",
                "sender": "bot"
            }
        ],
        "date_of_post": "2023-09-02T08:45:12Z",
        "data": "Vending Machines) located in Railway Sta...",
        "pdfsize": 438326,
        "pdfname": "ticket.pdf"
    },
    // Add other chat data as needed...
  ];
  private readonly baseUrl = 'YOUR_BACKEND_URL_HERE';
  constructor(private http: HttpClient) { }

  // Fetch all chat histories
  getChatHistories(): Observable<Chat[]> {
    return this.http.get<Chat[]>(`${this.baseUrl}/chat-histories`);
  }

  // Fetch specific chat details by ID
  getChatById(id: number) {
    return this.chats.find(chat => chat.id === id);
  }


  getChatDetails(id: number): Chat {
    return this.chats.find(chat => chat.id === id)!;  // Use `find` to retrieve the chat with the matching id.
 }
 
  
}