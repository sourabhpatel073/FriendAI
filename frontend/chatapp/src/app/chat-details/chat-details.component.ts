import { Component ,OnInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ChatDataService } from '../chat-data.service';
import { Chat } from '../chat.model';

@Component({
  selector: 'app-chat-details',
  templateUrl: './chat-details.component.html',
  styleUrls: ['./chat-details.component.css']
})
export class ChatDetailsComponent implements OnInit {
  chat: Chat = {
    id: 0,
    user_id: '',
    messages: [],
    date_of_post: '',
    data: '',
    pdfsize: 0,
    pdfname: ''
  };
  

  constructor(private chatDataService: ChatDataService,
    private route: ActivatedRoute) {}


  ngOnInit(): void {
    const chatId = +(this.route.snapshot.paramMap.get('id') ?? '0');


 // Convert string to number
    this.chat = this.chatDataService.getChatDetails(chatId);
  }
}

