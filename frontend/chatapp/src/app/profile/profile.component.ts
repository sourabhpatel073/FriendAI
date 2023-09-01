import { Component } from '@angular/core';
import { UserDataService } from '../user-data.service';
@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  userData: any;
  usernameFromLocalStorage: string = '';

  constructor(private userDataService: UserDataService) {}

  ngOnInit(): void {
    this.usernameFromLocalStorage = localStorage.getItem('user') || '';
    const userId = +localStorage.getItem('userId')!;  // Using + to convert the string to a number

    this.userDataService.getUserProfile(userId).subscribe(data => {
      this.userData = data;
    });
  }
}
