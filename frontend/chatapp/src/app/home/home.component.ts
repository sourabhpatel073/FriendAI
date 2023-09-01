import { Component,OnInit } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { ChatbotService } from '../chatbot.service';
import { MatDialog } from '@angular/material/dialog';
import { LoadingDialogComponent } from '../loading-dialog/loading-dialog.component';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  selectedPDFs: File[] = [];
  chat: {user: string, message: string}[] = [];
  userInput: string = '';
  chatHistory: {sender: string, message: string}[] = [];
  script:string=""
  pdfname:string=""
  pdfsize:string=""

  constructor(private http: HttpClient, private chatbotService: ChatbotService,private dialog: MatDialog) {} 
  ngOnInit(): void {
    // Add any initialization logic here if needed
    
  }
  onFileChange(event: any): void {
    const newFiles = Array.from(event.target.files) as File[];
    this.selectedPDFs = [...this.selectedPDFs, ...newFiles];
}
  removeSelectedPDF(pdf: File): void {
    if (Array.isArray(this.selectedPDFs)) {
        this.selectedPDFs = this.selectedPDFs.filter(item => item !== pdf);
    }
    (<HTMLInputElement>document.getElementById('pdfs')).value = '';
}



  uploadPDFs(): void {
    if (this.selectedPDFs.length === 0) {
       alert("Please select at least one PDF.");
     
      return;
    }

    const formData = new FormData();
    for (const pdf of this.selectedPDFs) {
      formData.append('pdfs', pdf);
    }

    // Replace with your API endpoint
    const dialogRef = this.dialog.open(LoadingDialogComponent);
    fetch("http://127.0.0.1:8000/galaxy/upload_pdfs/", {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      dialogRef.close();
      console.log(data.data)
      // this.script=JSON.stringify(data.data)
      this.pdfname=data.pdfname
      this.pdfsize=data.pdfsize
      alert("document Uploaded successfully");
      this.askChatbot("give summary");
    })
    .catch(error => {
      console.error("There was an error uploading the PDFs:", error);
    });
  }

  // processPDFs(): void {
  //   // Implement PDF processing logic here
  //   this.askChatbot("give summary");
  // }

  askChatbot(question: string): void {
    const dialogRef = this.dialog.open(LoadingDialogComponent);
    const url = 'http://localhost:8000/galaxy/ask_question/';

    // Format the body as x-www-form-urlencoded
    const body = new URLSearchParams();
    body.set('question', question);

    // Set the content-type header
    const headers = new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
    });

    // Make the POST request
    this.http.post(url, body.toString(), { headers: headers }).subscribe((response: any) => {
        if (response.status === 'error') {
            console.error(response.message);
            return;
        }

        // Add user's question to chat history
        this.chatHistory.push({ message: question, sender: 'user' });

        // Add bot's response to chat history
        this.chatHistory.push({ message: response.bot_response, sender: 'bot' });

        // Clear user input
        this.userInput = '';
        dialogRef.close();
        console.log(this.chatHistory)
    });
}


saveChatHistory() {
  const userId = localStorage.getItem('userId');
  
  // Ensure user ID exists
  if (!userId) {
      console.error('User ID not please login.');
      return;
  }

  let dataAll:any={
    messages:this.chatHistory,
    data:this.script,
    pdfsize:this.pdfsize,
    pdfname:this.pdfname
  }

  this.chatbotService.saveChatToBackend(dataAll, userId).subscribe(
      response => {
        alert("Chat saved successfully")
          console.log('Chat history saved successfully', response);
      },
      error => {
          console.error('Error saving chat history', error);
      }
  );
}

}
