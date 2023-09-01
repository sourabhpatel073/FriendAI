import { Component, OnInit } from '@angular/core';
import { ChatDataService } from '../chat-data.service';

interface Chat {
  id: number;
  user_id: string;
  messages: { message: string; sender: string; }[];
  date_of_post: string;
  pdfsize: number;
  pdfname: string;
}

@Component({
  selector: 'app-chat-history-list',
  templateUrl: './chat-history-list.component.html',
  styleUrls: ['./chat-history-list.component.css']
})
export class ChatHistoryListComponent implements OnInit {
  chatHistories: Chat[] = [];
  selectedChat: Chat | null = null;
  userId!: string;

  constructor(private chatDataService: ChatDataService) { }

  ngOnInit(): void {
    // Get user_id from localStorage
    this.userId = localStorage.getItem('userId') || '';

    // Fetch chats and filter by user_id
    this.chatDataService.getChatHistories().subscribe(chats => {
      this.chatHistories = chats.filter(chat => chat.user_id === this.userId);
    });
  }

  deleteChat(chatId: number): void {
    this.chatDataService.deleteChat(chatId).subscribe(() => {
      // Refresh the chat list after deleting a chat
      this.chatDataService.getChatHistories().subscribe(chats => {
        this.chatHistories = chats;
      });
    });
  }
   showDetails(chat: Chat): void {
    this.selectedChat = chat;
  }

  // Method to hide the detailed view
  closeDetails(): void {
    this.selectedChat = null;
  }
}
