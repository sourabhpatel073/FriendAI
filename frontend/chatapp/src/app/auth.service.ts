import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';
@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private _isUserAuthenticated = new BehaviorSubject<boolean>(false);
  readonly isUserAuthenticated = this._isUserAuthenticated.asObservable();

  constructor(private http: HttpClient, private router: Router) { }

  signup(username: string, email: string, password: string): void {
    // Modify the URL as per your backend endpoint
    const url = 'http://localhost:8000/galaxy/user_register/';
    const body = { username, email, password ,userprofile:{}    };

    this.http.post(url, body).subscribe(response => {
      // Handle successful signup, for example by setting user authentication status
      this._isUserAuthenticated.next(true);
      this.router.navigate(['/login'])
    }, error => {
      console.log(error)
    });
  }

  login(email: string, password: string): void {
    // Modify the URL as per your backend endpoint
    const url = 'http://localhost:8000/galaxy/user_login/';
    const body = { email, password };

    this.http.post(url, body).subscribe(response => {
      // Handle successful login, for instance by storing a token and setting user authentication status
      console.log(response)
      this._isUserAuthenticated.next(true);
      this.router.navigate(['/home'])
    }, error => {
      console.log(error)
    });
  }
}
