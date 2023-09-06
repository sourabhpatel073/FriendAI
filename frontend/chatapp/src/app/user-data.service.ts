import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserDataService {

  private readonly baseUrl = 'https://friendai.onrender.com/galaxy';

  constructor(private http: HttpClient) { }

  getUserProfile(userprofile_id: number): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/get_profile/${userprofile_id}/`);
  }

  updateUserProfile(userData: any): Observable<any> {
    const userId = userData.id;
    return this.http.patch<any>(`${this.baseUrl}/user/edit/${userId}/`, userData);
  }
}
