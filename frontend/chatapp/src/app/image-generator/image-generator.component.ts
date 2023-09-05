import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-image-generator',
  templateUrl: './image-generator.component.html',
  styleUrls: ['./image-generator.component.css']
})
export class ImageGeneratorComponent {
  description: string = '';
  generatedImageUrl: string = '';
  isLoading: boolean = false;
  constructor(private http: HttpClient) {}

  generateImage() {
    const apiUrl = 'http://localhost:8000/galaxy/generate-image/';
    const body = { "prompt": this.description };
    this.isLoading = true;
    this.http.post<any>(apiUrl, body).subscribe(response => {
        // Assuming the Django backend responds with the URL of the generated image
        console.log(response)
        this.generatedImageUrl = response.data.data[0].url; // adjust this path based on your Django's response structure
        this.isLoading = false;  
      });
}
}