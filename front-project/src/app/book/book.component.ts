import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api/api.service';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.css']
})
export class BookComponent implements OnInit {

  books : any;
  constructor(private api : ApiService) { }

  ngOnInit(){
    this.api.getAllBooks().subscribe(data =>{
      this.books = data;
      console.log(this.books);
      
    })
  }

}
