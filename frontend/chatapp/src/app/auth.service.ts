import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private _isUserAuthenticated = new BehaviorSubject<boolean>(false);
  readonly isUserAuthenticated = this._isUserAuthenticated.asObservable();

  constructor(private http: HttpClient) { }

  signup(username: string, email: string, password: string): void {
    // Modify the URL as per your backend endpoint
    const url = 'http://localhost:8000/galaxy/user_register/';
    const body = { username, email, password };

    this.http.post(url, body).subscribe(response => {
      // Handle successful signup, for example by setting user authentication status
      this._isUserAuthenticated.next(true);
    }, error => {
      // Handle signup errors, e.g. show a notification to the user
    });
  }

  login(email: string, password: string): void {
    // Modify the URL as per your backend endpoint
    const url = 'http://localhost:8000/galaxy/user_login/';
    const body = { email, password };

    this.http.post(url, body).subscribe(response => {
      // Handle successful login, for instance by storing a token and setting user authentication status
      this._isUserAuthenticated.next(true);
    }, error => {
      // Handle login errors, e.g. notify the user
    });
  }
}
