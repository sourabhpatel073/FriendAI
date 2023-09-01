import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserDataService {

  private readonly baseUrl = 'http://localhost:8000/galaxy';

  constructor(private http: HttpClient) { }

  getUserProfile(userId: number): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/get_profile/${userId}/`);
  }
}
