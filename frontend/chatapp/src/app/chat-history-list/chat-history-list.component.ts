import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ChatDataService } from '../chat-data.service';
interface Chat {
  id: number;
  user_id: string;
  messages: { message: string; sender: string; }[];
  date_of_post: string;
  data: string;
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

  constructor(private chatDataService: ChatDataService) { }

  ngOnInit(): void {
    this.chatDataService.getChatHistories().subscribe(chats => {
      this.chatHistories = chats;
    });
  }
}