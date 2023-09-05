import React , {Component} from 'react'

export default class BoxClass extends Component { //필기시험 낼수도...!
    constructor(props) { //생성자
        super(props);
        this.state = {
            city : '서울',
            국적 : '대한민국',
            cnt : 0,
            num : 0,
            value : 0,
        }
    }

    count = () => {
        this.setState({cnt : this.state.cnt+1});
    }

    render() { // Class 컴포넌트에서는 render 함수 필요 (무조건!)




        return (
            <div>
                <h1>Class Component, <br/> {this.props.name} in {this.state.city} {this.state.국적}</h1>
                <p>클릭 횟수 : {this.state.cnt}</p>
                <button onClick={this.count}>클릭</button>
            </div>
        )
    }
}