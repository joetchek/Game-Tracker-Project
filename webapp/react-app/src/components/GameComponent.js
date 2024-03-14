import Accordian from 'react-bootstrap/Accordion'
import { useAccordionButton } from 'react-bootstrap/esm/AccordionButton';
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'

function CardToggle({children, eventKey}) {
    const buttonOnClick = useAccordionButton(eventKey, () => {
        console.log('Button pressed');
    })

    //need to continue working on this
    return(
       <Button
        type='button'
        variant='dark'
        className='fs-5'
        onClick={buttonOnClick}>
            {children}
        </Button>     
    );
}

//passing in the game data as props
const GameComponent = (props) => {

    return(

        <Accordian defaultActiveKey="1">
            <Card className='text-center'>
                <Card.Header>
                    <CardToggle eventKey='0'>Name: {props.name}</CardToggle>
                </Card.Header>
                <Accordian.Collapse eventKey='0'>
                    <Card.Body variant='light'>
                        <Row className='fs-6'>
                            <Col className='border border-dark'>ID: {props.id}</Col>
                            <Col className='border border-dark'>Rating: {props.rating}</Col>
                            <Col className='border border-dark'>Date Released: NA</Col>
                        </Row>
                        <Row className='fs-6'>
                            <Col className='border border-dark'>Date Completed: NA</Col>
                            <Col className='border border-dark'>Hours: NA</Col>
                            <Col className='border border-dark'>Platform: NA</Col>
                        </Row>
                    </Card.Body>
                </Accordian.Collapse>
            </Card>
        </Accordian>

    );
}

export default GameComponent;