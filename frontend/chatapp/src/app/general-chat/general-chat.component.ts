import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface ChatMessage {
  sender: string;
  content: string;
}

interface ApiResponse {
    answer: string;
    // You can add more fields if your API response contains more information.
}

@Component({
  selector: 'app-general-chat',
  templateUrl: './general-chat.component.html',
  styleUrls: ['./general-chat.component.css']
})

export class GeneralChatComponent {
  context: string = '';
  tone: string = 'parent';
  question: string = '';
  language: string = 'english';
  chatMessages: ChatMessage[] = [];
  isTyping: boolean = false;

  constructor(private http: HttpClient) { }

  sendMessage() {
      const data = {
          context: this.context,
          tone: this.tone,
          question: this.question,
          language: this.language
      };
      this.isTyping = true; 
      this.http.post<ApiResponse>('https://friendai.onrender.com/galaxy/ask/', data).subscribe(response => {
          this.chatMessages.push({
              sender: 'user',
              content: this.question
          });
          this.chatMessages.push({
              sender: 'assistant',
              content: response.answer
          });
          this.isTyping = false; 
          this.question = '';  // Clear the question input
      });
  }
}
