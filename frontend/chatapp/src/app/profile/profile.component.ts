import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { UserDataService } from '../user-data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  profileForm!: FormGroup;
  userData: any;
  isEditing: boolean = false;

  constructor(private formBuilder: FormBuilder, private userDataService: UserDataService, private router: Router) {}

  ngOnInit() {
    this.fetchUserData();
  }
  fetchUserData() {
    const userprofile_id = +localStorage.getItem('userId')!;

    this.userDataService.getUserProfile(userprofile_id).subscribe(
      response => {
        this.userData = response;
        this.initForm();
      },
      error => {
        console.error('Error fetching user data:', error);
      }
    );
  }
  initForm() {
    this.profileForm = this.formBuilder.group({
      username: [this.userData.username],
      email: [this.userData.email],
      profile_picture: [this.userData.userprofile.profile_picture]
    });
  }

  editProfile() {
    if (this.isEditing) {  // This should be true when you're trying to save the data.
      const updatedProfile = this.profileForm.value;
  
      this.userDataService.updateUserProfile({
        id: this.userData.id,
        ...updatedProfile,
        userprofile: {
          ...this.userData.userprofile,
          profile_picture: updatedProfile.profile_picture
        }
      }).subscribe(response => {
        // Handle the success. Maybe set isEditing to false, or provide feedback to the user.
        console.log('Update successful', response);
        this.isEditing = false;
      }, error => {
        console.error('Error updating profile:', error);
      });
    } else {
      this.isEditing = true;  // This is when you want to start editing the profile.
    }
  }
  
  logout(){
    localStorage.removeItem('token');
    localStorage.removeItem("userId");
    this.router.navigate(['/home'])
  }
}
