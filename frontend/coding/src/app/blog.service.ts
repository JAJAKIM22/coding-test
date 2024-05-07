import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BlogService {

  private apiUrl = 'http://127.0.0.1:8000/blogs/';

  constructor(private http: HttpClient) { }

  getBlogs(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}
